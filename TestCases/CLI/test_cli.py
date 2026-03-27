import pytest
from Utilities.helper import run_command


@pytest.mark.cli
def test_docker_installed(logger):
    logger.info("STEP: Verify Docker installation")

    result = run_command(["docker", "--version"])

    logger.info(f"STDOUT: {result.stdout}")
    logger.info(f"STDERR: {result.stderr}")

    assert result.returncode == 0, "Docker is not installed"
    assert "docker" in result.stdout.lower(), "Invalid docker version output"

    logger.info("Docker installation verified successfully")


@pytest.mark.cli
def test_docker_daemon_running(logger):
    logger.info("STEP: Verify Docker daemon is running")

    result = run_command(["docker", "info"])

    logger.info(f"STDOUT: {result.stdout[:500]}")  # limit output
    logger.info(f"STDERR: {result.stderr}")

    assert result.returncode == 0, "Docker daemon is not running"

    logger.info("Docker daemon is running successfully")


@pytest.mark.cli
def test_docker_images_available(logger):
    logger.info("STEP: Verify Docker images availability")

    result = run_command(["docker", "images"])

    logger.info(f"STDOUT:\n{result.stdout}")
    logger.info(f"STDERR: {result.stderr}")

    assert result.returncode == 0, "Failed to fetch Docker images"
    assert len(result.stdout.strip()) > 0, "No Docker images found"

    logger.info("Docker images are available")

@pytest.mark.cli
def test_docker_containers_running(logger):
    logger.info("STEP: Check Docker containers are running")

    result = run_command(["docker", "ps"])

    logger.info(f"Return Code: {result.returncode}")
    logger.info(f"STDOUT:\n{result.stdout}")
    logger.info(f"STDERR:\n{result.stderr}")

    # Validate docker command
    assert result.returncode == 0, "Docker command failed"

    output = result.stdout.lower()

    # Validate containers (based on your docker-compose)
    assert "selenium-hub" in output, "Selenium Hub is not running"
    assert "chrome" in output or "firefox" in output, "Browser container is not running"

    logger.info("Docker containers are running successfully")

@pytest.mark.cli
def test_docker_network_ls(logger):
    logger.info("STEP: Verify Docker networks listing")

    result = run_command(["docker", "network", "ls"])

    logger.info(f"STDOUT:\n{result.stdout}")
    logger.info(f"STDERR: {result.stderr}")

    assert result.returncode == 0, "Failed to fetch Docker networks"

    assert "NETWORK ID" in result.stdout, "Invalid network list output"

    assert "bridge" in result.stdout, "Default bridge network missing"

    logger.info("Docker networks listed successfully")