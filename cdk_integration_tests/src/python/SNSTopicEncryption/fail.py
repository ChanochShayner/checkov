from constructs import Construct
from aws_cdk import (
    App, 
    Stack,
    aws_sns as sns,
    aws_kms as kms
)


class MyStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        topic = sns.Topic(self, "Topic",
                          topic_name="my-topic",
                          )

app = App()
MyStack(app, "MyStack")
app.synth()
