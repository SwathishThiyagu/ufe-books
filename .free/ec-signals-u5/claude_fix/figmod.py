import importlib.util, os
_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'pipeline', 'claude_figs', 'ec_signals_u5.py')
_s = importlib.util.spec_from_file_location('ec_signals_u5', _p); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
spec = _m.spec; bank_svg = _m.bank_svg
