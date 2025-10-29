# RAG-Based Document Q&A System with AWS Bedrock. Deploying using AWS(lambda, ECR), Langchain, Huggingface, Docker

A production-ready Retrieval-Augmented Generation (RAG) application that enables intelligent question-answering over PDF documents using LangChain, AWS Bedrock, and Streamlit. The system leverages Amazon Titan embeddings and Meta LLaMA 3 for accurate, context-aware responses.

## 🌟 Features

- **PDF Document Processing**: Automatic ingestion and processing of PDF documents from a local directory
- **Vector Store with FAISS**: Efficient similarity search using Facebook AI Similarity Search
- **AWS Bedrock Integration**: Leverages Amazon Titan embeddings and Meta LLaMA 3 language model
- **Interactive Streamlit UI**: User-friendly interface for querying documents and managing vector stores
- **CI/CD Pipeline**: Automated GitHub Actions workflow for continuous integration and deployment
- **Docker Support**: Containerized application ready for deployment to AWS ECR/ECS
- **Scalable Architecture**: Modular design with separate ingestion and retrieval components

## 🏗️ Architecture

The application follows a modular architecture:

```
├── QASystem/
│   ├── ingestion.py              # Document loading and vector store creation
│   └── retrievalandgeneration.py # LLM setup and response generation
├── app.py                         # Streamlit web interface
├── Dockerfile                     # Container configuration
├── .github/workflows/main.yaml    # CI/CD pipeline
└── requirements.txt               # Python dependencies
```

### Key Components

1. **Data Ingestion Pipeline**: Loads PDFs, splits text into chunks, and creates vector embeddings
2. **Vector Store**: FAISS index for fast similarity search
3. **Retrieval QA Chain**: LangChain RetrievalQA with custom prompts
4. **AWS Bedrock Models**:
   - `amazon.titan-embed-text-v2:0` for embeddings
   - `meta.llama3-8b-instruct-v1:0` for text generation

## 📋 Prerequisites

- Python 3.10+
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials
- Docker (for containerization)
- GitHub account (for CI/CD)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

Create a `.env` file in the project root:

```bash
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
```

Or configure using AWS CLI:

```bash
aws configure
```

### 4. Prepare Your Documents

Create a `Data/` directory in the project root and add your PDF documents:

```bash
mkdir Data
cp your-documents.pdf Data/
```

## 💻 Usage

### Running Locally

1. **Start the Streamlit Application**:

```bash
streamlit run app.py
```

2. **Access the Web Interface**: Open your browser to `http://localhost:8501`

3. **Initialize Vector Store**:
   - Click "Update / Create Vectors" in the sidebar to process your PDFs
   - This creates a FAISS index from your documents

4. **Ask Questions**:
   - Enter your question in the text input
   - Click "Run Query with LLaMA 3" to get AI-powered answers

### Running with Docker

1. **Build the Docker Image**:

```bash
docker build -t rag-qa-system .
```

2. **Run the Container**:

```bash
docker run -p 8501:8501 \
  -e AWS_ACCESS_KEY_ID=your_key \
  -e AWS_SECRET_ACCESS_KEY=your_secret \
  -e AWS_DEFAULT_REGION=us-east-1 \
  -v $(pwd)/Data:/app/Data \
  rag-qa-system
```

## 🚢 Deployment

### GitHub Actions CI/CD

The project includes an automated deployment pipeline that:

1. **Continuous Integration**:
   - Lints code
   - Runs unit tests

2. **Continuous Delivery**:
   - Builds Docker image
   - Pushes to Amazon ECR
   - Ready for ECS deployment

### Required GitHub Secrets

Configure these secrets in your GitHub repository:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `AWS_ECR_REPO_URI`

### Manual Deployment to AWS

1. **Push to ECR**:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker tag rag-qa-system:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/rag-qa-system:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/rag-qa-system:latest
```

2. **Deploy to ECS**: Configure an ECS service to run the container


## 👤 Author

**Nikhil Advani**
- Email: nikhil.advani.ds@gmail.com

## 🙏 Acknowledgments

- Built with LangChain framework
- Powered by AWS Bedrock
- Vector search by FAISS
- UI by Streamlit

---

**Note**: This application requires active AWS Bedrock access and will incur AWS usage costs based on the number of API calls and tokens processed.

