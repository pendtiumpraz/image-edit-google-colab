# 🎨 AI Image Edit — Google Colab Notebooks

Koleksi **12 notebook** Google Colab untuk image editing menggunakan berbagai model AI open-source terbaik. Setiap model tersedia dalam versi **Pro** (A100/V100) dan **Free** (T4).

---

## 📋 Daftar Notebook

### 🔥 FireRed Image Edit
| Versi | File | GPU | Login? |
|-------|------|-----|--------|
| **Pro** | [`FireRed_Image_Edit_Pro.ipynb`](FireRed_Image_Edit_Pro.ipynb) | A100/V100 | ❌ Tidak perlu |
| **Free** | [`FireRed_Image_Edit_Free.ipynb`](FireRed_Image_Edit_Free.ipynb) | T4 | ❌ Tidak perlu |

> **Model:** `FireRedTeam/FireRed-Image-Edit-1.0`
> General-purpose image editing. Akurat, berkualitas tinggi, visual konsisten.

---

### 📜 Qwen Image Edit 2511
| Versi | File | GPU | Login? |
|-------|------|-----|--------|
| **Pro** | [`Qwen_Image_Edit_2511_Pro.ipynb`](Qwen_Image_Edit_2511_Pro.ipynb) | A100/V100 | ❌ Tidak perlu |
| **Free** | [`Qwen_Image_Edit_2511_Free.ipynb`](Qwen_Image_Edit_2511_Free.ipynb) | T4 | ❌ Tidak perlu |

> **Model:** `Qwen/Qwen-Image-Edit-2511`
> Character consistency terbaik, multi-person editing, LoRA support, style transfer.

---

### 🌀 OmniGen
| Versi | File | GPU | Login? |
|-------|------|-----|--------|
| **Pro** | [`OmniGen_Image_Edit_Pro.ipynb`](OmniGen_Image_Edit_Pro.ipynb) | A100/V100 | ❌ Tidak perlu |
| **Free** | [`OmniGen_Image_Edit_Free.ipynb`](OmniGen_Image_Edit_Free.ipynb) | T4 | ❌ Tidak perlu |

> **Model:** `Shitao/OmniGen-v1` · Lisensi: MIT
> Unified model — edit, generation, subject-driven dalam satu pipeline. Tanpa plugin tambahan.

---

### ⚡ FLUX.1 Kontext [dev]
| Versi | File | GPU | Login? |
|-------|------|-----|--------|
| **Pro** | [`FLUX_Kontext_Image_Edit_Pro.ipynb`](FLUX_Kontext_Image_Edit_Pro.ipynb) | A100/V100 | ⚠️ Perlu |
| **Free** | [`FLUX_Kontext_Image_Edit_Free.ipynb`](FLUX_Kontext_Image_Edit_Free.ipynb) | T4 | ⚠️ Perlu |

> **Model:** `black-forest-labs/FLUX.1-Kontext-dev` · 12B parameter · **Gated model**
> Kualitas editing terbaik, contextual understanding, konsisten multi-edit.
>
> 🔑 Accept terms dulu: https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev

---

### 🎯 Z-Image-Edit
| Versi | File | GPU | Login? |
|-------|------|-----|--------|
| **Pro** | [`ZImage_Edit_Pro.ipynb`](ZImage_Edit_Pro.ipynb) | A100/V100 | ⚠️ Perlu |
| **Free** | [`ZImage_Edit_Free.ipynb`](ZImage_Edit_Free.ipynb) | T4 | ⚠️ Perlu |

> **Model:** `Tongyi-MAI/Z-Image-Edit` · Alibaba · 6B parameter · **Gated model**
> Instruction-following akurat, natural language prompt editing, bilingual EN/CN.
>
> 🔑 Accept terms dulu: https://huggingface.co/Tongyi-MAI/Z-Image-Edit

---

### ⚡ FLUX.2 Klein
| Versi | File | GPU | Model | Login? |
|-------|------|-----|-------|--------|
| **Pro** | [`FLUX2_Klein_Image_Edit_Pro.ipynb`](FLUX2_Klein_Image_Edit_Pro.ipynb) | A100/V100 | 9B | ⚠️ Perlu |
| **Free** | [`FLUX2_Klein_Image_Edit_Free.ipynb`](FLUX2_Klein_Image_Edit_Free.ipynb) | T4 | 4B (Apache 2.0) | ⚠️ Perlu |

> **Model:** `black-forest-labs/FLUX.2-klein-9B` / `4B` · **Gated model**
> Sub-second inference! Model paling cepat. 4B version cocok untuk T4.
>
> 🔑 Accept terms dulu: https://huggingface.co/black-forest-labs/FLUX.2-klein-9B

---

## 🚀 Fitur Semua Notebook

Setiap notebook dilengkapi **Gradio UI** dengan tab-tab berikut:

| Tab | Fungsi |
|-----|--------|
| 🖼️ **Single Edit** | Upload 1 gambar → 1 prompt → 1 output |
| 🖼️ **Multi-Image** | 2-3 gambar sekaligus *(FireRed & Qwen only)* |
| 📦 **Bulk Edit** | 1 prompt → semua gambar di folder. Nama file output **sama** dengan input |
| 🎨 **Multi-Prompt (1×N)** | 1 gambar × banyak prompt → banyak output |
| 📦🎨 **Multi-Prompt (N×N)** | Banyak gambar × banyak prompt → kombinasi penuh |
| 📁 **Drive Browser** | Browse folder Google Drive langsung dari UI |

### 📂 Google Drive Integration
- Input gambar dari Google Drive
- Output otomatis tersimpan ke Google Drive
- Folder output per model:
  - `MyDrive/FireRed-Output/`
  - `MyDrive/Qwen-ImageEdit-Output/`
  - `MyDrive/OmniGen-Output/`
  - `MyDrive/FluxKontext-Output/`
  - `MyDrive/ZImage-Output/`
  - `MyDrive/Flux2Klein-Output/`

### 📦 Bulk Edit
```
Input folder:  MyDrive/Photos/MyFolder/
                 ├── photo1.jpg
                 ├── photo2.png
                 └── photo3.webp

Output folder: MyDrive/FireRed-Output/bulk/
                 ├── photo1.jpg    ← nama sama!
                 ├── photo2.png
                 └── photo3.webp
```

### 🎨 Multi-Prompt (N×N)
```
Prompts (1 per baris):
  Make it watercolor
  Make it pencil sketch
  Make it pop art

Output:
  output/prompt_1/photo1.jpg   ← watercolor
  output/prompt_1/photo2.jpg
  output/prompt_2/photo1.jpg   ← pencil sketch
  output/prompt_2/photo2.jpg
  output/prompt_3/photo1.jpg   ← pop art
  output/prompt_3/photo2.jpg
```

---

## 🆚 Perbandingan Model

| Model | Kualitas | Kecepatan | T4 Friendly | Multi-Image | Keunggulan |
|-------|----------|-----------|-------------|-------------|------------|
| **FireRed** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | General-purpose, stabil |
| **Qwen 2511** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | Character consistency, LoRA |
| **OmniGen** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ✅ | All-in-one, tanpa plugin |
| **FLUX Kontext** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⚠️ | ✅ | Kualitas terbaik, kontekstual |
| **Z-Image-Edit** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⚠️ | ❌ | Alibaba, bilingual |
| **FLUX.2 Klein** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ (4B) | ✅ | **Paling cepat!** Sub-second |

---

## 📖 Cara Pakai

### 1. Upload ke Colab
- Buka [Google Colab](https://colab.research.google.com/)
- `File → Upload notebook` → pilih file `.ipynb`

### 2. Set GPU
- `Runtime → Change runtime type → GPU`
  - **Pro**: pilih A100 atau V100
  - **Free**: pilih T4

### 3. Jalankan Cell
- Jalankan cell **1 → 2 → 3 → 4** secara berurutan
- Cell terakhir akan membuka **Gradio UI** dengan link public

### 4. Edit Gambar!
- Buka link Gradio yang muncul
- Upload gambar atau browse dari Google Drive
- Tulis prompt dan klik Generate! 🎉

---

## ⚠️ Catatan Penting

### Pro vs Free
| | Pro | Free |
|---|---|---|
| GPU | A100 / V100 | T4 |
| Precision | bfloat16 (full) | float16 + CPU offload |
| Max Resolution | Unlimited | 512-768px (auto-resize) |
| Speed | Cepat | Lebih lambat |
| VRAM | 40-80GB | 15GB |
| Colab | Colab Pro/Pro+ | Colab gratis |

### Model Gated (⚠️)
Untuk FLUX Kontext, Z-Image-Edit, dan FLUX.2 Klein:
1. Buka link model di HuggingFace
2. Klik **"Agree and access repository"**
3. Buat token di https://huggingface.co/settings/tokens
4. Paste token saat diminta `login()` di Colab

### Tips Menghindari OOM (Out of Memory)
- Gunakan versi **Free** untuk T4
- Kurangi **MaxRes** (slider di UI)
- Kurangi **Steps** 
- Proses gambar satu-satu, bukan bulk

---

## 📁 Struktur Folder

```
colab/
├── README.md
├── FireRed_Image_Edit_Pro.ipynb
├── FireRed_Image_Edit_Free.ipynb
├── Qwen_Image_Edit_2511_Pro.ipynb
├── Qwen_Image_Edit_2511_Free.ipynb
├── OmniGen_Image_Edit_Pro.ipynb
├── OmniGen_Image_Edit_Free.ipynb
├── FLUX_Kontext_Image_Edit_Pro.ipynb
├── FLUX_Kontext_Image_Edit_Free.ipynb
├── ZImage_Edit_Pro.ipynb
├── ZImage_Edit_Free.ipynb
├── FLUX2_Klein_Image_Edit_Pro.ipynb
└── FLUX2_Klein_Image_Edit_Free.ipynb
```

---

## 📜 Lisensi Model

| Model | Lisensi |
|-------|---------|
| FireRed | Apache 2.0 |
| Qwen 2511 | Apache 2.0 |
| OmniGen | MIT |
| FLUX.1 Kontext | FLUX.1-dev Non-Commercial |
| Z-Image-Edit | Tongyi License |
| FLUX.2 Klein 9B | Non-Commercial |
| FLUX.2 Klein 4B | Apache 2.0 ✅ |
