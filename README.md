# baidu-tr-async-free ![Python package](https://github.com/ffreemt/baidu-tr-async-free/workflows/Python3.6|3.7%20package/badge.svg)[![codecov](https://codecov.io/gh/ffreemt/baidu-tr-async-free/branch/master/graph/badge.svg)](https://codecov.io/gh/ffreemt/baidu-tr-async-free)
baidu translate for free with async and proxy support

### Installation
Not available yet
```pip install baidu-tr-async```

Validate installation
```
python -c "import bdtr_async; print(bdtr_async.__version__)"
0.0.1
```

### Usage

```
import asyncio
from bdtr_async import bdtr_async

asyncio.get_event_loop().run_until_complete(bdtr_async('test this and that'))
# '测试这个和那个'
```

### Acknowledgments

* Thanks to everyone whose code was used
