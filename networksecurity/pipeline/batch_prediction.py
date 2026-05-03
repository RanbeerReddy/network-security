import os
import sys
import pandas as pd
import numpy as np

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_transformation import DataTransformation
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.entity.artifact_entity import DataTransformationArtifact


class BatchPrediction:
    def __init__(self, input_file_path, model_path, preprocessor_path):
        self.input_file_path = input_file_path
        self.model_path = model_path
        self.preprocessor_path = preprocessor_path

    def start_batch_prediction(self):
        try:
            logging.info("Loading preprocessor and model")
            preprocessor = load_object(self.preprocessor_path)
            model = load_object(self.model_path)

            logging.info("Loading input data")
            df = pd.read_csv(self.input_file_path)

            # Assuming the input has the same columns as training data
            input_arr = preprocessor.transform(df)

            logging.info("Making predictions")
            predictions = model.predict(input_arr)

            # Add predictions to dataframe
            df['prediction'] = predictions

            # Save predictions
            prediction_file_path = os.path.join("prediction_output", "predictions.csv")
            os.makedirs(os.path.dirname(prediction_file_path), exist_ok=True)
            df.to_csv(prediction_file_path, index=False)

            logging.info(f"Batch prediction completed. Results saved to {prediction_file_path}")
            return prediction_file_path

        except Exception as e:
            raise NetworkSecurityException(e, sys)