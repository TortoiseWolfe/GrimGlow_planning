#!/bin/bash
# Swap GPU between Ollama (openclaw) and ComfyUI (GrimGlow).
# RTX 3060 Ti 8GB can only run one at a time.

GRIMGLOW_DIR="$HOME/repos/GrimGlow_planning"
OPENCLAW_DIR="$HOME/repos/openclaw"

case "$1" in
  comfyui)
    echo "Unloading Ollama models to free GPU..."
    docker exec openclaw-ollama-1 ollama stop 2>/dev/null
    sleep 3
    echo "Starting ComfyUI..."
    docker compose -f "$GRIMGLOW_DIR/docker-compose.yml" up -d
    echo "ComfyUI starting at http://localhost:8188"
    echo "(First launch downloads ComfyUI — may take a few minutes)"
    ;;
  ollama)
    echo "Stopping ComfyUI..."
    docker compose -f "$GRIMGLOW_DIR/docker-compose.yml" down
    echo "GPU freed for Ollama."
    ;;
  status)
    echo "=== GPU ==="
    nvidia-smi --query-gpu=name,memory.used,memory.free --format=csv,noheader
    echo ""
    echo "=== ComfyUI ==="
    docker compose -f "$GRIMGLOW_DIR/docker-compose.yml" ps 2>/dev/null || echo "Not running"
    echo ""
    echo "=== Ollama ==="
    docker exec openclaw-ollama-1 ollama ps 2>/dev/null || echo "Not reachable"
    ;;
  *)
    echo "Usage: gpu-swap.sh {comfyui|ollama|status}"
    echo "  comfyui  - Free GPU from Ollama, start ComfyUI"
    echo "  ollama   - Stop ComfyUI, free GPU for Ollama"
    echo "  status   - Show GPU and container status"
    exit 1
    ;;
esac
