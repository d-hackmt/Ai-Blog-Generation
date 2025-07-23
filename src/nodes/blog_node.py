from src.states.blogstate import BlogState

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
