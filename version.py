class Version:
    _major_versions_number = 0
    _minor_versions_number = 1
    _versions_string = "beta"

    @classmethod
    def get_version_string(cls) -> str:
        return f"{cls._major_versions_number}.{cls._minor_versions_number} {cls._versions_string}"
