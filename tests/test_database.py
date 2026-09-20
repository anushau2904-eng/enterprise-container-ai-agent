from database.db_manager import get_all_containers


def test_get_all_containers():
    containers = get_all_containers()

    print("\nContainers:")
    for container in containers:
        print(container)

    assert containers is not None
    assert len(containers) > 0