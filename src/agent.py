from autogen import AssistantAgent, UserProxyAgent

def create_agent():
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
    assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
    user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
    return assistant, user_proxy