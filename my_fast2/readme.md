pip install fastapi
pip install pydantic
pip install uvicorn

FastAPI是一个现代、高性能、易于使用的Python Web框架,用于构建API和Web应用程序。

以下是FastAPI的一些主要特点:

- 基于标准的Python类型注解自动生成 OpenAPI文档。这使得编写文档变得非常简单直观。

- 提供了路由系统和装饰器,可以非常简洁地定义API端点。

- 自动请求数据验证和序列化。

- 高性能 - 基于Starlette和Pydantic,性能接近NodeJS和Go。

- 支持异步请求处理。 

- 自动生成OpenAPI schemas。

- 容易调试。

- 支持各种数据库后端,包括SQLAlchemy、MongoDB等。

- 可以轻松地与多种身份验证系统集成,包括OAuth2。

- 有大量的扩展提供额外的功能。

- 良好的文档和开发者社区。

总之,FastAPI是一个非常易学和使用的Web框架,适合构建快速、可扩展且容易维护的现代API。它的性能、功能集和文档都非常出色。

======

FastAPI与Flask的速度对比:

1. 启动时间:

- FastAPI启动时间通常在50-60毫秒左右。
- Flask启动时间在300-500毫秒左右,比FastAPI慢了约10倍。

2. 平均响应时间:

- 对简单请求,FastAPI的平均响应时间在1-2毫秒左右。
- Flask的平均响应时间在5-10毫秒左右,比FastAPI慢了5-10倍。

3. 最大吞吐量:

- FastAPI在基准测试下可以达到每秒约15,000请求的最大吞吐量。
- Flask最大吞吐量约为每秒2,000请求,不到FastAPI的1/7。 

4. 并发性能:

- FastAPI利用异步和Python最新async/await语法,可以实现很好的并发处理能力。
- Flask的并发能力较弱,性能会下降很快。

所以总体来说,FastAPI的速度大约比Flask快5-10倍,这主要归功于以下技术:

- 基于Starlette使用uvloop异步网络库。
- 使用Pydantic进行数据验证和序列化。
- 使用异步语法,而Flask是同步框架。
- 优化的代码和路由结构。

但是Flask有更丰富的扩展生态和 longer history。

所以对于性能要求高的API服务,FastAPI是一个更好的选择。而Flask适用于更广泛的web应用场景。