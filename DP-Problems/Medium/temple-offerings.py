def offerings(N, arr):
    # Create an array to store the offerings with at least 1 offering for each temple
    offerings = [1] * N

    # Left to right pass: ensuring temples higher than their previous get more offerings
    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            offerings[i] = offerings[i - 1] + 1

    # Right to left pass: ensuring temples higher than their next get more offerings
    for i in range(N - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            offerings[i] = max(offerings[i], offerings[i + 1] + 1)

    # Sum the total offerings to get the minimum number of offerings required
    return sum(offerings)
