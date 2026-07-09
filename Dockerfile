FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime
WORKDIR /workspace
COPY requirements.txt pyproject.toml environment.yml README.md ./
COPY code ./code
COPY settings ./settings
COPY manifests ./manifests
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -e .
ENV PYTHONPATH=/workspace/code
