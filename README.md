Build the image:

```bash
docker build -t optimization-test .
```

Run the image:

```bash
docker run -it --rm optimization-test bash
```

Run the solver:

```bash
python knapsack.py
```
