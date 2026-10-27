#!/usr/bin/env python3
"""Auditoría opcional: python scripts/auditar_origen.py CARPETA_CON_PORTFOLIO_PROFILE_TRANSCRIPT_JSON"""
import json,sys,collections,datetime
from pathlib import Path
if len(sys.argv)!=2:sys.exit('Uso: python scripts/auditar_origen.py /ruta/con/json')
p=Path(sys.argv[1]);
def read(name):
 with (p/f'{name}.json').open(encoding='utf-8') as f:
  return [json.loads(x) for x in f if x.strip()]
o,pf,t=(read(x) for x in ('portfolio','profile','transcript'))
for name,rows in [('portfolio',o),('profile',pf),('transcript',t)]:
 print(f'{name}: {len(rows):,} filas; {len(rows[0])} columnas; tipos:',{k:type(v).__name__ for k,v in rows[0].items()})
print('Nulos en profile:',{k:sum(v.get(k) is None for v in pf) for k in pf[0]})
print('Edades marcadas 118:',sum(v['age']==118 for v in pf))
print('Duplicados exactos transcript:',len(t)-len({json.dumps(x,sort_keys=True) for x in t}))
print('Horas:',min(v['time'] for v in t),max(v['time'] for v in t))
print('Eventos:',dict(collections.Counter(v['event'] for v in t)))
cents=sum(round(100*v['value']['amount']) for v in t if v['event']=='transaction')
print('Volumen USD:',f'{cents/100:,.2f}')
