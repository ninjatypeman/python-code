# Python Code

1. 安装第三方库

```bash
# 临时使用清华源安装 requests 和 bs4 库（或者尝试魔法TUN）
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple requests bs4
# PowerShell 运行：python demo.py
```

- HTTP 请求

```python
# 返回的是 Response 类实例；<Response [200]>
print(response)
# HTTP 状态码是 200，请求成功；418 状态码表示客户端错误 (I'm a teapot)
print(response.status_code)
# 打印 HTML 源码
print(response.text)
```

- HTTP 请求头会包含一些给服务器的信息，比如 User-Agent

- VSCode Python 代码格式化工具：autopep8

- Xpath，Beautiful Soup, 正则；写入 .csv；JSON，八爪鱼


