"""
This is a boilerplate pipeline 'sum'
generated using Kedro 0.19.12
"""

from kedro.pipeline import Pipeline, node
from .nodes import compute_sum

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=compute_sum,
                inputs="input_numbers",
                outputs="output_sum",
                name="sum_node"
            )
        ]
    )

