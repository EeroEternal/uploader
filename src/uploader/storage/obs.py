"""Huawei obs function."""
import tomllib


def obs_config(filepath):
    """Read obs config from toml file.

    Args:
        filepath (str): toml config file path.
    Returns:
        (str, str, str, str): access_id, secret_key, endpoint, bucket.
    """
    with open(filepath, "rb") as f:
        config = tomllib.load(f)

        access_key_id = config["obs"]["access_key_id"]
        secret_access_key = config["obs"]["secret_access_key"]
        endpoint = config["obs"]["endpoint"]
        bucket = config["obs"]["bucket"]
        return access_key_id, secret_access_key, endpoint, bucket


def upload_images(images, config_file):
    """Upload images to obs.

    Args:
        images (List[Image]): image list.
        config_file (str): config file path.
    """
    access_key_id, secret_access_key, endpoint, bucket = obs_config(config_file)
    client = Client(access_key_id, secret_access_key, endpoint)

    for image in images:
        client.put_object(bucket, image.name, image.content)