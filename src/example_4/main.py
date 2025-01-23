import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf/case_1", config_name="config")
def my_app(cfg : DictConfig) -> None:
    OmegaConf.resolve(cfg)
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
