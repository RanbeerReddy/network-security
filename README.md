# 🔒 Network Security ML Pipeline

A comprehensive machine learning pipeline for detecting phishing attacks using advanced data processing, model training, and cloud deployment. This project demonstrates end-to-end MLOps practices with MongoDB, AWS S3, MLflow tracking, and automated CI/CD.

## 🚀 Features

- **Data Ingestion**: Automated data extraction from MongoDB collections
- **Data Validation**: Drift detection and data quality checks using Evidently
- **Data Transformation**: Feature engineering and preprocessing pipelines
- **Model Training**: Multiple ML algorithms with hyperparameter tuning
- **Model Evaluation**: Comprehensive metrics and MLflow experiment tracking
- **Model Deployment**: Flask API for real-time predictions
- **Cloud Integration**: AWS S3 for artifact storage and model versioning
- **MLOps**: Complete CI/CD pipeline with Docker containerization
- **Monitoring**: Logging and error handling throughout the pipeline

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+**
- **Machine Learning**: Scikit-learn, XGBoost, Imbalanced-learn
- **Data Processing**: Pandas, NumPy
- **Web Framework**: Flask

### Databases & Storage
- **MongoDB**: NoSQL database for raw data storage
- **AWS S3**: Cloud storage for model artifacts and datasets

### MLOps & Experiment Tracking
- **MLflow**: Experiment tracking and model registry
- **DagShub**: Git-based MLflow tracking
- **Evidently**: Data drift detection and model monitoring

### DevOps & Deployment
- **Docker**: Containerization
- **GitHub Actions**: CI/CD automation
- **AWS ECR**: Container registry

### Development Tools
- **Jupyter Notebook**: Interactive development
- **Python-dotenv**: Environment management
- **Certifi**: SSL certificate handling

## 📋 Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account
- AWS account with S3 and ECR access
- DagShub account for MLflow tracking
- Docker (for containerized deployment)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/network-security.git
   cd network-security
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

5. **Set up environment variables**
   Edit the `.env` file with your:
   - MongoDB connection string
   - AWS credentials
   - MLflow tracking URI and credentials
   - DagShub token

## 🚀 Usage

### Data Pipeline Execution

1. **Push data to MongoDB**
   ```bash
   python push_data.py
   ```

2. **Run the complete ML pipeline**
   ```bash
   python main.py
   ```

3. **Start the prediction API**
   ```bash
   python app.py
   ```

### API Endpoints

The Flask API provides the following endpoints:

- `GET /` - Health check
- `POST /predict` - Real-time phishing detection

Example prediction request:
```json
{
  "features": {
    "feature1": 0.5,
    "feature2": 1.2,
    // ... other features
  }
}
```

## 📁 Project Structure

```
networksecurity/
├── components/
│   ├── data_ingestion.py      # MongoDB data extraction
│   ├── data_transformation.py # Feature engineering
│   ├── data_validation.py     # Data quality checks
│   └── model_trainer.py       # ML model training
├── pipeline/
│   ├── training_pipeline.py   # Main training workflow
│   └── batch_prediction.py    # Batch prediction pipeline
├── cloud/
│   └── s3_syncer.py          # AWS S3 integration
├── utils/
│   ├── main_utils/           # Core utilities
│   └── ml_utils/             # ML-specific utilities
├── constant/
│   └── training_pipeline/    # Configuration constants
├── entity/
│   ├── config_entity.py      # Configuration classes
│   └── artifact_entity.py    # Artifact definitions
├── exception/
│   └── exception.py          # Custom exception handling
├── logging/
│   └── logger.py            # Logging configuration
└── __init__.py
```

## 🔄 CI/CD Pipeline

The project includes GitHub Actions workflows for:

- **Automated Testing**: Unit tests and integration tests
- **Code Quality**: Linting and formatting checks
- **Container Build**: Docker image creation and ECR push
- **Deployment**: Automated deployment to AWS

### GitHub Secrets Required

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```

## 📊 Model Performance

The pipeline supports multiple algorithms:
- Random Forest
- XGBoost
- Support Vector Machines
- Neural Networks

Models are evaluated on:
- Accuracy, Precision, Recall, F1-Score
- ROC-AUC curves
- Confusion matrices
- Feature importance analysis

## 🔍 Data Drift Monitoring

Integrated Evidently for:
- Data quality monitoring
- Model performance degradation detection
- Feature drift analysis
- Target drift detection

## 🐳 Docker Deployment

### Build and run locally
```bash
docker build -t network-security .
docker run -p 8080:8080 network-security
```

### EC2 Deployment Commands
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Ranbeer Reddy**
- LinkedIn: https://www.linkedin.com/in/ranbeerreddy-mukpogle-528b48290/
- Email: reddyranbeer@gmail.com
- GitHub: https://github.com/RanbeerReddy

## 🙏 Acknowledgments

- MongoDB Atlas for database hosting
- AWS for cloud infrastructure
- DagShub for MLflow hosting
- Evidently for data monitoring capabilities
- The open-source ML community

---

⭐ Star this repo if you find it helpful!