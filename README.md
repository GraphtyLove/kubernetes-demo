# kubernetes-demo

Small Demo to show how to deploy on Kubernetes

## API

The API is a simple FastAPI application.

### Build & push the image

```bash
docker build -t graphtylove/api-demo:latest .
docker push -t graphtylove/api-demo:latest
```

### Run locally

```bash
docker run -p 80:80 graphtylove/api-demo:latest
```

## Kubernetes

The Kubernetes manifests are in the `kubernetes` folder.

```bash
kubectl apply -f kubernetes/manifest.yaml
```
