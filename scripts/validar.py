#!/usr/bin/env python3
"""Comprobación reproducible de datos del dashboard (sin dependencias externas)."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent
d=json.loads((p/'data/resumen.json').read_text(encoding='utf-8'))
ref=json.loads((p/'validacion.json').read_text(encoding='utf-8'))
groups=list(d['groups'].values())
assert sum(v['cents'] for v in groups)==ref['total_cents'], 'Ventas incorrectas'
assert sum(v['tx'] for v in groups)==ref['transactions'], 'Transacciones incorrectas'
assert sum(v['users'] for v in groups)==ref['members'], 'Clientes incorrectos'
assert [sum(g['offers'][i][j] for g in groups for i in range(10)) for j in range(3)]==ref['offer_events'], 'Eventos de ofertas incorrectos'
assert d['quality']['events']==ref['rows'], 'Cantidad de eventos inconsistente'
for g in groups:
    assert sum(g['days'])==g['cents'], 'Suma por día incorrecta'
    assert sum(v[1] for v in g['age'].values())==g['cents'], 'Suma por edad incorrecta'
    assert sum(v[1] for v in g['years'].values())==g['cents'], 'Suma por alta incorrecta'
    assert sum(g['bins'])==g['tx'], 'Histograma incorrecto'
assert d['groups']['F']['tx']==49382 and d['groups']['F']['cents']==86369500
print('APROBADO: ventas US$1,775,451.97; 138,953 transacciones; 17,000 clientes; 76,277 recibidas, 57,725 vistas y 33,579 completadas. Filtro F aprobado.')
