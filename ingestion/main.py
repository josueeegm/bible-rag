import os
import requests
import time
import json

endpoint = os.environ["DOC_INTELLIGENCE_ENDPOINT"]
key = os.environ["DOC_INTELLIGENCE_KEY"]

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/pdf"
}

output_dir = "/data"
input_dir = "/pdfs"

for file in os.listdir(input_dir):
    if file.endswith(".pdf"):
        with open(os.path.join(input_dir, file), "rb") as f:
            resp = requests.post(f"{endpoint}/formrecognizer/documentModels/prebuilt-read:analyze?api-version=2023-07-31",
                                 headers=headers, data=f)
            operation = resp.headers["operation-location"]

        # Wait for result
        while True:
            result = requests.get(operation, headers={"Ocp-Apim-Subscription-Key": key}).json()
            if result.get("status") in ["succeeded", "failed"]:
                break
            time.sleep(2)

        if result["status"] == "succeeded":
            pages = result["analyzeResult"]["content"]
            out_path = os.path.join(output_dir, file.replace(".pdf", ".json"))
            with open(out_path, "w") as out:
                json.dump({"content": pages}, out)

