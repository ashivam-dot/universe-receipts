"""Focused local tests of the actual proposed functions, without cloud/LLM imports."""
from pathlib import Path
from datetime import datetime, timezone
from types import SimpleNamespace
import ast,json,statistics,tempfile,unittest
SOURCE=Path(__file__).resolve().parents[1]/'src/ytc/auto.py'
KEEP={'_publication_time','_early_reach','_reviews','_video_rows','_median','_section','update_learnings'}
def namespace():
    tree=ast.parse(SOURCE.read_text());nodes=[ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0)]
    nodes += [n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in KEEP]
    nodes += [n for n in tree.body if isinstance(n,ast.Assign) and 'MAX_RULES' in ast.unparse(n.targets[0])]
    ns={'datetime':datetime,'Path':Path,'IST':timezone.utc,'statistics':statistics,'json':json,'re':__import__('re'),
        '_json':lambda p,default=None:json.loads(p.read_text()) if p.exists() else default,
        'yaml':SimpleNamespace(safe_load=lambda text:{'beats':[{'text':'the hook'}]}),
        '_by_video':lambda eps:{e['video_id']:e for e in eps}}
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),str(SOURCE),'exec'),ns)
    return ns
class MeasurementTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.ns=namespace()
    def tearDown(self):self.tmp.cleanup()
    def episode(self,id,day,checkpoint=700,hours=25.1):
        folder=self.root/id;folder.mkdir();(folder/'script.json').write_text('{}');(folder/'short.yaml').write_text('unused')
        perf={'24':{'numbers':{'hours':hours,'views':checkpoint},'verdict':'observed','diagnosis':{'worked':[],'hurt':[],'change_next':'test'}}}
        (folder/'performance.json').write_text(json.dumps(perf))
        ep={'id':id,'folder':folder,'video_id':id,'series':'space','title':id,'record':{'sent_at':f'2026-10-{day:02}T23:00:00Z'}}
        video={'id':id,'published':ep['record']['sent_at'],'title':id,'views':10000,'likes':10,'comments':0,'analytics':{}}
        return ep,video
    def test_publication_order_not_episode_id(self):
        older,v1=self.episode('ep999',1);newer,v2=self.episode('ep001',22)
        rows=self.ns['_video_rows']({'videos':[v2,v1]},[newer,older])
        self.assertEqual([r['short'] for r in rows],['ep999','ep001'])
        self.assertEqual(self.ns['_reviews']([newer,older],count=1)[0]['short'],'ep001')
    def test_early_reach_separate_from_lifetime_and_missing_retention(self):
        ep,v=self.episode('ep001',22,700);row=self.ns['_video_rows']({'videos':[v]},[ep])[0]
        self.assertEqual(row['early_reach'],{'hours':25.1,'views':700});self.assertEqual(row['views'],10000)
        self.assertIsNone(row['avg_viewed']);self.assertIsNone(row['subs'])
    def test_missing_or_late_checkpoints_remain_unknown(self):
        ep,v=self.episode('ep001',22,700,hours=45)
        self.assertIsNone(self.ns['_early_reach'](ep['folder']))
        (ep['folder']/'performance.json').write_text(json.dumps({'72':{'numbers':{'hours':73,'views':800}}}))
        self.assertIsNone(self.ns['_early_reach'](ep['folder']))
    def test_learning_baseline_and_board_use_checkpoint_and_unknown_subscribers(self):
        ep,v=self.episode('ep001',22,700);file=self.root/'LEARNINGS.md'
        file.write_text('# Log\n\n## What to beat\n\n## Rules we\'ve proven\n\n## Hypotheses to test\n\n## Scoreboard\n\n## Log\n')
        captured=[]
        def generate(prompt,**kwargs):
            captured.append(prompt);return {'reasons':[],'rules':[],'hypotheses':[],'summary':'test','log':'test'}
        self.ns.update({'episodes':lambda:[ep],'_sister_rules':lambda:'','LEARNINGS':file,'LEARN_FROM_HOURS':24,'LEARN_SCHEMA':{},
                        'llm':SimpleNamespace(generate=generate),'_now':lambda:datetime.now(timezone.utc)})
        result=self.ns['update_learnings'](None,{'videos':[v]})
        self.assertEqual(result['medians']['early_views'],700);self.assertIsNone(result['medians']['subs_per_1000'])
        self.assertIn('Observed 24-30h views',file.read_text());self.assertIn('| 700 |',file.read_text())
        self.assertIn('Missing early_reach or Analytics is unknown',captured[0])
    def test_rules_need_four_measured_shorts_and_are_capped(self):
        ep,v=self.episode('ep001',22,700);file=self.root/'LEARNINGS.md'
        file.write_text('# Log\n\n## What to beat\n\n## Rules we\'ve proven\n\n## Hypotheses to test\n\n## Scoreboard\n\n## Log\n')
        captured=[]
        def generate(prompt,**kwargs):
            captured.append(prompt)
            return {'reasons':[],'rules':[f'rule {i}' for i in range(15)],'hypotheses':[f'hyp {i}' for i in range(12)],
                    'summary':'test','log':'test'}
        self.ns.update({'episodes':lambda:[ep],'_sister_rules':lambda:'','LEARNINGS':file,'LEARN_FROM_HOURS':24,'LEARN_SCHEMA':{},
                        'llm':SimpleNamespace(generate=generate),'_now':lambda:datetime.now(timezone.utc)})
        self.ns['update_learnings'](None,{'videos':[v]})
        text=file.read_text()
        self.assertIn('- rule 9\n',text);self.assertNotIn('rule 10',text)
        self.assertIn('- hyp 7\n',text);self.assertNotIn('hyp 8',text)
        self.assertIn('4 or more Shorts show the same effect AND',captured[0]);self.assertIn('at most 10 rules',captured[0])
if __name__=='__main__':unittest.main(verbosity=2)
