from src.states.blogstate import BlogState
from langchain_core.messages import HumanMessage
from src.states.blogstate import Blog


class BlogNode:
    """
    A class to represent blog node
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        Create the title for the blog
        """
        if "topic" in state and state["topic"]:
            prompt = """
            You are an expert blog content writer. 
            Use Markdown formatting.
            Generate a blog title for the topic: {topic}.
            This title should be creative and SEO friendly.
            make sure the title is only within 6-10 words
            Give only 1 title , no extra information
            """
            system_message = prompt.format(topic=state["topic"])
            print(system_message)

            response = self.llm.invoke(system_message)
            print(response)

            return {"blog": {"title": response.content}}

    def content_generation(self, state: BlogState):
        """
        Create detailed blog content
        """
        if "topic" in state and state["topic"]:
            system_prompt = """
            You are an expert blog content writer. 
            Use Markdown formatting.
            Generate a detailed blog post with a complete breakdown 
            for the topic: {topic}.
            """
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {
                "blog": {
                    "title": state.get('blog', {}).get('title', ''),
                    "content": response.content
                }
            }

        
    def translation(self, state: BlogState):
        """
        Translate the content to a specified language
        """
        translation_prompt = """
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT: 
        {blog_content}
        """
        blog_content = state["blog"]["content"]
        messages = [
            HumanMessage(
                translation_prompt.format(
                    current_language=state["current_language"],
                    blog_content=blog_content
                )
            )
        ]

        translation_content = self.llm.with_structured_output(Blog).invoke(messages)

        return {
            "blog": {
                "title": state["blog"]["title"],
                "content": translation_content.content
            }
        }
        
        
    def route(self , state:BlogState):
        return {"current_langauge":state['current_language']}
    
    
    def route_decision(self,state:BlogState):
        """ 
        
        Route the content to the respective translation function
        
        """
        
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            return state["current_language"]