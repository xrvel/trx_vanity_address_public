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
```

### ✅ On Windows

1. Download and install Python 3 from [python.org](https://www.python.org/downloads/)
2. Install required packages:
```bash
pip install ecdsa base58 "eth-hash[pycryptodome]"
```

---

## 🚀 Installation

### Installing tmux (if not already installed)

#### On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install tmux
```

#### On Linux (CentOS/RHEL/AlmaLinux):
```bash
sudo dnf install tmux
# or
sudo yum install tmux
```

#### On macOS:
```bash
brew install tmux
```

#### On Windows:
```bash
# Using Chocolatey
choco install tmux

# Using Scoop
scoop install tmux
```

---

## 🎯 Usage

### Command Line Options

The `go.py` script supports the following options:

- `--prefix PREFIX`: Desired prefix (starts after the T in the address)
- `--suffix SUFFIX`: Desired suffix at the end of the address
- `--case-sensitive`: Enable case-sensitive matching (default is case-insensitive)

### Examples

```bash
# Generate address with prefix "abc"
python3 go.py --prefix abc

# Generate address with suffix "xyz"
python3 go.py --suffix xyz

# Generate address with both prefix and suffix
python3 go.py --prefix abc --suffix xyz

# Generate address with case-sensitive matching
python3 go.py --prefix ABC --case-sensitive
```

### Running with tmux

Since generating vanity addresses can take a long time, it's recommended to run the script in a tmux session:

#### Starting a new tmux session:
```bash
tmux new-session -d -s vanity_address
```

#### Attaching to the session:
```bash
tmux attach-session -t vanity_address
```

#### Running the script in tmux:
```bash
# Inside the tmux session
python3 go.py --prefix abc
```

#### Detaching from tmux (keeping the session running):
Press `Ctrl+B`, then `D`

#### Reattaching to the session later:
```bash
tmux attach-session -t vanity_address
```

#### Listing all tmux sessions:
```bash
tmux list-sessions
```

#### Killing a tmux session:
```bash
tmux kill-session -t vanity_address
```

---

## 📊 Output

### Console Output

When a matching address is found, the script displays:
- ✅ Success message with attempt count
- The generated TRON address
- The private key (in hexadecimal format)
- Time spent generating
- Speed (attempts per second)

### vanity_result.txt Output

When an address is found, the following information is appended to `vanity_result.txt`:

```
Address: T[generated_address]
Private Key: [64-character_hexadecimal_private_key]
Attempts: [number_of_attempts]
Time spent: [time_in_seconds] sec
Speed: [attempts_per_second] attempts/sec
-----
```

Example:
```
Address: Tabc123xyz456789abcdef
Private Key: 601ccc2e5e30189b287cb2c1963b063be319275221c026c2a826bdbb649d96e8
Attempts: 15420
Time spent: 12.34 sec
Speed: 1250.00 attempts/sec
-----
```

---

## 🔧 Additional Tools

### check.py
A utility script to verify private keys and display their corresponding TRON addresses.

Usage:
```bash
python3 check.py
```

---

## ⚡ Performance Tips

- **Longer prefixes/suffixes** take exponentially more time to generate
- **Case-sensitive matching** is slower than case-insensitive
- The script shows progress every 1000 attempts
- Use tmux to keep the process running even if you disconnect

---

## 🔒 Security Note

⚠️ **Important**: Keep your private keys secure! Anyone with access to the private key can control the TRON address and its funds. Never share your private keys with anyone.

---

## 📝 License

This project is open source and available under the MIT License.
