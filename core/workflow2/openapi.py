from typing import Any


def build_workflow_openapi() -> dict[str, Any]:
    return {
        "openapi": "3.1.0",
        "info": {
            "title": "Quantis Workflow API",
            "version": "0.6.0-beta.12",
        },
        "paths": {
            "/workflows": {
                "get": {
                    "operationId": "listWorkflowDefinitions",
                    "responses": {"200": {"description": "Workflow definitions"}},
                }
            },
            "/workflows/{workflow_id}": {
                "get": {
                    "operationId": "getWorkflowDefinition",
                    "parameters": [
                        {
                            "name": "workflow_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "responses": {"200": {"description": "Workflow definition"}},
                }
            },
            "/workflow-instances": {
                "post": {
                    "operationId": "createWorkflowInstance",
                    "responses": {"201": {"description": "Workflow instance created"}},
                }
            },
            "/workflow-instances/{instance_id}": {
                "get": {
                    "operationId": "getWorkflowInstance",
                    "responses": {"200": {"description": "Workflow instance"}},
                }
            },
            "/workflow-instances/{instance_id}/run": {
                "post": {
                    "operationId": "runWorkflowInstance",
                    "responses": {"200": {"description": "Workflow instance executed"}},
                }
            },
            "/human-tasks/{task_id}/complete": {
                "post": {
                    "operationId": "completeHumanTask",
                    "responses": {"200": {"description": "Human task completed"}},
                }
            },
        },
    }
