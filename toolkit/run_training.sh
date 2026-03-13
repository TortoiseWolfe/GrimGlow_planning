#!/bin/bash
# Train GrimGlow multi-character LoRA on SDXL
# Run from GrimGlow_planning repo root:
#   docker compose stop comfyui
#   docker compose --profile training run --rm kohya-trainer bash /toolkit/run_training.sh

set -e

echo "=== GrimGlow Character LoRA Training ==="
echo "Model: SDXL 1.0"
echo "Dataset: 29 images, 6 characters"
echo "Target: /output/grimglow_characters.safetensors"
echo ""

# Verify GPU
python3 -c "import torch; print(f'GPU: {torch.cuda.get_device_name(0)}, VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f}GB')"

# Build dataset config TOML (sd-scripts format)
cat > /tmp/dataset_config.toml << 'EOF'
[general]
resolution = 1024
enable_bucket = true
caption_extension = ".txt"

[[datasets]]
batch_size = 1

  [[datasets.subsets]]
  image_dir = "/dataset/grimglow_sable"
  num_repeats = 20

  [[datasets.subsets]]
  image_dir = "/dataset/grimglow_wren"
  num_repeats = 20

  [[datasets.subsets]]
  image_dir = "/dataset/grimglow_jink"
  num_repeats = 20

  [[datasets.subsets]]
  image_dir = "/dataset/grimglow_thresh"
  num_repeats = 20

  [[datasets.subsets]]
  image_dir = "/dataset/grimglow_luma"
  num_repeats = 20

  [[datasets.subsets]]
  image_dir = "/dataset/grimglow_theodore"
  num_repeats = 25
EOF

echo "Dataset config written."
echo "Starting training..."
echo ""

python3 /opt/sd-scripts/sdxl_train_network.py \
  --pretrained_model_name_or_path="/checkpoints/sd_xl_base_1.0.safetensors" \
  --dataset_config="/tmp/dataset_config.toml" \
  --output_dir="/output" \
  --output_name="grimglow_characters" \
  --save_model_as="safetensors" \
  --max_train_steps=3000 \
  --learning_rate=1e-4 \
  --optimizer_type="AdamW8bit" \
  --mixed_precision="bf16" \
  --full_bf16 \
  --seed=42 \
  --cache_latents \
  --cache_latents_to_disk \
  --cache_text_encoder_outputs \
  --gradient_checkpointing \
  --network_module="networks.lora" \
  --network_dim=32 \
  --network_alpha=16 \
  --network_train_unet_only \
  --save_every_n_steps=1000 \
  --logging_dir="/output/logs"

echo ""
echo "=== Training complete ==="
ls -lh /output/grimglow_characters*
