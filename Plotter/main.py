import os
import dotenv
import autogen

dotenv.load_dotenv()


def main():
    llm_config = {
        "cache_seed": 48,
        "temperature": 0,
        "config_list": [{
          "model": "gpt-4-turbo",
          "api_key": os.getenv("OPENAI_API_KEY"),
        }],
        
    }
    user_proxy = autogen.UserProxyAgent(
      name="Admin",
      system_message="""
      A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.
      """,
      human_input_mode="NEVER",
      code_execution_config={
        "work_dir": ".\\Pruebas\\coding",
        "use_docker": False
      }
    )

    researcher = autogen.AssistantAgent(
      name="Researcher",
      system_message="""
       Financial Researcher
      Gather all of the necessary financial information, using search tools, about a company for the financial analyst to prepare a report. 
      An expert financial researcher, who spends all day and night thinking about financial performance of different companies.
      Use a search tool to look up this company's stock information: company_name. 
    The goal is to prepare enough information to make an informed analysis of the company's stock performance.
        All of the relevant financial information about the company's stock performance.
     """,
      llm_config=llm_config,
    )
    analyst = autogen.AssistantAgent(
      name="Financial Analyst",
      system_message="""
          Financial Analyst
      Take provided company financial information and create a thorough financial report about a given company.
      An expert financial analyst who prides themselves on creating clear and easily readable financial reports of different companies.
      Take company_name's financial information, analyze it, and provide a financial analysis, including: Profitability ratio,
      Liquidity ratios, Solvency ratios, Efficiency ratios, Growth metrics, Valuation metrics, and Cash flow metrics.
      A nicely formatted analysis including all of the financial metrics necessary for a thorough financial analysis of a company.
      """,
      llm_config=llm_config,
    )
    plotter = autogen.AssistantAgent(
      name="Plotter",
      system_message="""
         Plotter.
         Your job is plot a chart of how the company's sotck price change.
      """,
      llm_config=llm_config,
    )
    group_chat = autogen.GroupChat(
      agents=[user_proxy, researcher, analyst, plotter],
      messages=[],
    )
    manager = autogen.GroupChatManager(
      groupchat=group_chat,
      llm_config=llm_config
    )
    user_proxy.initiate_chat(
      manager,
      message="I need information of Tesla"
    )


if __name__ == "__main__":
    main()
