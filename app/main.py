from fastapi import FastAPI
from app.api.v1 import external
from .core.exception_handlers import register_exception_handlers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ACL CS2 External API",
    version="1.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)
app.include_router(external.router)
# origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,  # 允许的域名列表
    allow_origin_regex=r"https?://.*",
    allow_credentials=True,  # 是否允许携带 Cookie、Authorization 头等凭证
    allow_methods=["*"],  # 允许的 HTTP 方法，["GET","POST",...] 或 ["*"]
    allow_headers=["*"],  # 允许的请求头，或者写具体的 header 列表
    max_age=600,  # 预检请求（OPTIONS）的缓存时间，单位秒
)
register_exception_handlers(app)
