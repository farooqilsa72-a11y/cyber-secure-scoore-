def cyber_security_score(vulnerabilities, patch_level, firewall_strength, password_strength, encryption_level):
    """
    Each factor is rated from 0 to 100
    Higher score = better security
    """

    # Weighted scoring model
    score = (
        (100 - vulnerabilities) * 0.30 +   # fewer vulnerabilities = better
        patch_level * 0.20 +
        firewall_strength * 0.20 +
        password_strength * 0.15 +
        encryption_level * 0.15
    )

    return round(score, 2)


# Example input (0–100 scale)
vulnerabilities = 20        # 20% weak points
patch_level = 80            # system updates
firewall_strength = 85
password_strength = 70
encryption_level = 90

score = cyber_security_score(
    vulnerabilities,
    patch_level,
    firewall_strength,
    password_strength,
    encryption_level
)

print("Cyber Security Score:", score)
