# End-to-End Blog Generation with Agentic AI

This is an end-to-end backend application for generating blogs using agentic flows powered by LangGraph and FastAPI. The system supports multiple versions of blog generation including translation to different languages using LLMs.

This project is **backend only** and does **not include a frontend UI**. You can use Postman or any REST client to interact with the APIs.

---

##  Project Structure

```
.
├── app.py                        # FastAPI app with blog generation endpoints
├── demo_request.json            # Example request payloads for v1 and v2
├── langgraph.json               # Optional config for LangGraph
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .env                         # API keys and environment variables
├── .gitignore
├── v1 v2 images/                # Sample screenshots or logs for v1 and v2 output
└── src/
    ├── graphs/
    │   └── graph_builder.py     # Graph structure builder with conditional flows
    ├── llms/
    │   └── groqllm.py           # Groq LLM wrapper
    ├── nodes/
    │   └── blog_node.py         # Blog-related node logic (title, content, translation)
    └── states/
        └── blogstate.py         # State definition for blog generation
```

---

## 🔌 API Endpoint

### `POST /blogs`

This is the main endpoint for generating blogs.

---

## 💡 Sample Requests

| Version | Description                                     | Sample Input |
|---------|-------------------------------------------------|--------------|
| **v1**  | Basic blog generation with topic only           | `{ "topic": "Agentic AI" }` |
| **v2**  | Blog generation with topic and desired language | `{ "topic": "Agentic AI", "language": "French" }` |

Refer to the `demo_request.json` file for these examples.

---

## 🚀 How to Run

1. Clone the repository
2. Set up your `.env` file with your GROQ and LANGCHAIN API keys.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the FastAPI server:

```bash
python app.py
```

5. Open [http://localhost:8000/docs](http://localhost:8000/docs) to view Swagger API docs.

---

##  LangSmith Tracing

This app integrates with LangSmith for tracing and debugging LLM calls in the LangGraph flow. You must set the following environment variables:

```env
LANGCHAIN_TRACING=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=Blog_Generation_v1
```

Make sure your FastAPI app is running while using LangGraph Studio to visualize flow.

---

##  Tech Stack

- LangGraph – Graph-based flow controller for agentic applications
- FastAPI – Lightweight web framework for serving APIs
- Postman – For testing API requests
- LangSmith – For tracing, observability and debugging LLM flow

---

##  Version Outputs

Check the `v1 v2 images/` folder for visual examples of v1 and v2 request outputs.

---

##  Contributions

Feel free to open issues or submit pull requests to improve the app or extend its functionality.

---

## Thank you for checking out this project!
