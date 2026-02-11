def clean_name(raw_name):
    """Normalize full name text and keep only alphabetic parts."""
    normalized = " ".join(raw_name.strip().lower().split())
    parts = normalized.split(" ")

    valid_parts = []
    for part in parts:
        # Keep only alphabetic characters from each part
        letters_only = ""
        for char in part:
            if char.isalpha():
                letters_only += char
        if letters_only:
            valid_parts.append(letters_only)

    return valid_parts


def clean_domain(raw_domain):
    """Normalize and validate domain input."""
    domain = raw_domain.strip().lower()

    # Remove common protocols if user enters them
    if domain.startswith("https://"):
        domain = domain[8:]
    elif domain.startswith("http://"):
        domain = domain[7:]

    # Remove leading www.
    if domain.startswith("www."):
        domain = domain[4:]

    # Remove trailing slash
    if domain.endswith("/"):
        domain = domain[:-1]

    return domain


def build_email_options(name_parts, domain):
    """Create email ID options using string operations only."""
    first_name = name_parts[0]
    last_name = name_parts[-1] if len(name_parts) > 1 else ""

    options = []
    options.append(first_name + "@" + domain)

    if last_name:
        options.append(first_name + "." + last_name + "@" + domain)
        options.append(first_name + "_" + last_name + "@" + domain)
        options.append(first_name[0] + last_name + "@" + domain)
        options.append(first_name + last_name[0] + "@" + domain)

    # Optional number variants
    options.append(first_name + "123@" + domain)
    if last_name:
        options.append(first_name + "." + last_name + "2026@" + domain)

    # Remove duplicates while preserving order
    unique_options = []
    for email in options:
        if email not in unique_options:
            unique_options.append(email)

    return unique_options


def main():
    print("=" * 40)
    print("📧 Professional Email Generator")
    print("=" * 40)

    full_name = input("Enter your full name: ")
    domain_input = input("Enter your domain (e.g., company.com): ")

    name_parts = clean_name(full_name)
    domain = clean_domain(domain_input)

    if not name_parts:
        print("\n❌ Invalid name. Please enter alphabetic characters.")
        return

    if not domain or "." not in domain:
        print("\n❌ Invalid domain. Example: gmail.com")
        return

    email_options = build_email_options(name_parts, domain)

    print("\n✅ Suggested Email IDs:")
    print("-" * 40)
    for index, email in enumerate(email_options, start=1):
        print(str(index) + ". " + email)

    print("-" * 40)
    print("Tip: Choose a short and professional option.")


if __name__ == "__main__":
    main()
