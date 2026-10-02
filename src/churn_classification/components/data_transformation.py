import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from src.churn_classification.logger import logger
from src.churn_classification.entity.config_entity import DataTransformationConfig


class DataTransformation:

    def __init__(self, config : DataTransformationConfig):
        self.config = config
        self.scaler = None
        self.pipeline = None

    def data_train_test_split(self):
        try:
            data = pd.read_csv(self.config.data_path)
            data = data.drop(columns=['CustomerID'])
            data.columns = data.columns.str.replace(" ", "")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logger.info("Data transformation completed successfully.")
        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e
        return train_data, test_data
        
    def init_pipeline(self, standardizer_type='standard'):
        if standardizer_type == 'standard':
            self.scaler = StandardScaler()
        elif standardizer_type == 'robust':
            self.scaler = RobustScaler()
        elif standardizer_type == 'minmax':
            self.scaler = MinMaxScaler()
        else:
            raise ValueError(f"Unsupported standardizer type: {standardizer_type}. Supported types are 'standard', 'robust', and 'minmax'.")
        
        ordinal_ContractLength = OrdinalEncoder(categories=[["Monthly","Quarterly","Annual"]])
        ordinal_SubscriptionType = OrdinalEncoder(categories=[["Basic","Standard","Premium"]])
        onehot_gender = OneHotEncoder(drop="if_binary",sparse_output=False,handle_unknown="ignore")
        self.pipeline = ColumnTransformer(
            transformers=[
            ('standard_scaler', self.scaler, ['Age','Tenure','UsageFrequency','SupportCalls','PaymentDelay','TotalSpend','LastInteraction']),
            ('onehot_gender',onehot_gender,['Gender']),
            ('ordinal_contractLength', ordinal_ContractLength, ['ContractLength']),
            ('ordinal_subscriptionType', ordinal_SubscriptionType, ['SubscriptionType'])
        ],
        verbose_feature_names_out=False
        )
    def combine_x_y(self, X, y):
        if len(X) != len(y):
            raise Exception("length of X and y are different")
        X_df= pd.DataFrame(X, columns=self.pipeline.get_feature_names_out(),index=y.index)
        data=pd.concat([X_df, y], axis=1)
        return data

    def get_transformed_data(self):
        train, test = self.data_train_test_split()
        x_train = train.drop(columns=[self.config.target_column])
        x_test = test.drop(columns=[self.config.target_column])
        y_train = train[self.config.target_column]
        y_test = test[self.config.target_column]
        self.init_pipeline()
        x_train_transformed = self.pipeline.fit_transform(x_train)
        x_test_transformed = self.pipeline.transform(x_test)
        train=self.combine_x_y(x_train_transformed,y_train)
        test=self.combine_x_y(x_test_transformed,y_test)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
        
        logger.info("Split data into training and test sets")
        print(train.head())
        print(test.head())



    