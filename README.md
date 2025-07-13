# 🪙 TRON Vanity Address Generator

This Python script generates TRON (TRX) addresses with a custom **vanity prefix and/or suffix** — such as `Tabc123xyz`.

Ideal for creating branded or personalized addresses for TRON wallets.

---

## 📦 Requirements

### ✅ On Linux (AlmaLinux 9, CentOS, Ubuntu)

Install Python 3 and pip:

```bash
# Install Python 3
dnf install python3 -y

# Install pip
dnf install python3-pip -y

# Install required Python packages with Keccak backend
pip3 install ecdsa base58 "eth-hash[pycryptodome]"
