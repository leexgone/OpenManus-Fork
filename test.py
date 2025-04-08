import asyncio
import sys

from pydantic import Field

from app.agent.manus import Manus

# from app.agent.planning import PlanningAgent
from app.logger import logger

# from app.tool import Terminate, ToolCollection
# from app.tool.file_saver import FileSaver
from app.tool.python_execute import PythonExecute
from app.tool.str_replace_editor import StrReplaceEditor
from app.tool.web_search import WebSearch


async def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else input("请输入你的分析指令：")
    if not prompt.strip():
        logger.error("未输入有效的分析指令。")
        return

    logger.info("开始执行分析...")

    agent = Manus()
    # agent.available_tools.add_tools(
    #     WebSearch(),
    #     # FileSaver(),  # PythonExecute(), StrReplaceEditor()
    # )
    # agent.max_steps = 50
    # agent.available_tools = Field(
    #     default_factory=lambda: ToolCollection(
    #         WebSearch(),
    #         PythonExecute(),
    #         StrReplaceEditor(),
    #         FileSaver(),
    #         Terminate(),
    #     )
    # )
    await agent.run(prompt)

    logger.info("分析执行完成！")
    # logger.info(result)


if __name__ == "__main__":
    asyncio.run(main())
