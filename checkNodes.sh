for host in juno3 juno4 juno6 juno7; do
    echo "===== $host ====="
    ssh $host "top -b -n 1 | head -n 15"
done
