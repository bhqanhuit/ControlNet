import argparse



def build_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_root_dir", type=str, default="./training")
    parser.add_argument("--vae_load_path", type=str, default="./ckpts/VITONHD_VAE_finetuning.ckpt")
    parser.add_argument("--batch_size", "-bs",  type=int, default=32)
    parser.add_argument("--save_every_n_epochs", type=int, default=20)
    parser.add_argument("--max_epochs", type=int, default=1000)
    parser.add_argument("--save_root_dir", type=str, default="./logs")
    parser.add_argument("--save_name", type=str, default="dummy")
    parser.add_argument("--img_H", type=int, default=512)
    parser.add_argument("--img_W", type=int, default=384)
    parser.add_argument("--learning_rate", type=float, default=1e-4)
    parser.add_argument("--device", type=str, default="cuda")


    opt = parser.parse_args()
    return opt