from langgraph.graph import StateGraph , START ,  END

from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
        
    
    def build_topic_graph(self):
        """
        
        Build a graph to generate blogs based on topic
        
        """
        
        self.blog_node_obj = BlogNode(self.llm)
        
        
        ## nodes
        self.graph.add_node("title_creation" , self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation" , self.blog_node_obj.content_generation)
        
        ## edges 
        
        self.graph.add_edge(START , "title_creation")       
        self.graph.add_edge("title_creation" , "content_generation")       
        self.graph.add_edge("content_generation" ,END)
        
        
        return self.graph        
    
    
    def build_language_graph(self):
        """ 
        Build a graph for blog genereation
        with inputs topic and language 
        
        """
        
        self.blog_node_obj = BlogNode(self.llm)
        
        ## nodes
        self.graph.add_node("title_creation" , self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation" , self.blog_node_obj.content_generation)
        
        ## ** state means - all the values which we give as key value pairs will be overridden
        
        self.graph.add_node("hindi_translation" , lambda state:self.blog_node_obj.translation({**state, "current_language":"hindi"}))
        self.graph.add_node("french_translation" , lambda state:self.blog_node_obj.translation({**state, "current_language":"french"}))
        self.graph.add_node("route" , self.blog_node_obj.route)
        
        
        ## edges and condtional edges
        
        # edges
        
        self.graph.add_edge(START , "title_creation")       
        self.graph.add_edge("title_creation" , "content_generation")       
        self.graph.add_edge("content_generation" , "route")
        
        # conditonal edge
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "hindi" : "hindi_translation",
                "french" : "french_translation"
            }
        )
        
        # end edges
        
        self.graph.add_edge("hindi_translation" , END)
        self.graph.add_edge("french_translation" , END)
        
        return self.graph
        
    # for multiple functionalities
    def setup_graph(self,usecase):
        if usecase == "topic":
            self.build_topic_graph()
        if usecase == "language":
            self.build_language_graph()
        
        
        return self.graph.compile()
    
    
## Below code is for the langsmith langgraph studio

llm = GroqLLM().get_llm()

## get the graph

graph_builder = GraphBuilder(llm)
graph = graph_builder.build_language_graph().compile()