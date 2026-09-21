#!/usr/bin/env bash
# Codespace birinchi marta yaratilganda bir marta bajariladi
set -e
python -m pip install --user -r requirements.txt
chmod +x *.sh
./gen.sh
curl -sSL https://github.com/fullstorydev/grpcurl/releases/download/v1.9.4/grpcurl_1.9.4_linux_x86_64.tar.gz \
  | sudo tar -xz -C /usr/local/bin grpcurl
echo "---- tayyor ----"
python -c "import grpc; print('grpcio', grpc.__version__)"
grpcurl -version
docker --version
