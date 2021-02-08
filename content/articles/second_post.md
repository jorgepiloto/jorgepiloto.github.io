Title: A second post!
Subtitle: A subtitle for the post
Date: 2020-02-01
Category: Orbital mechanics
Tags: pelican, publishing
Slug: second-post
Authors: Jorge M.G.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sit amet
vulputate arcu, in posuere augue. Interdum et malesuada fames ac ante ipsum
primis in faucibus. Cras vel ex eget velit vehicula lobortis. Donec sodales orci
tortor, auctor egestas erat pretium a. Integer gravida nec lectus sed posuere.
Nunc eros est, rhoncus ut iaculis quis, imperdiet sed massa. Quisque et ipsum ac
tortor posuere ullamcorper. Nullam pharetra ultricies ornare. Vestibulum in
vestibulum augue.

## A section
Orci varius natoque penatibus et magnis dis parturient montes, nascetur
ridiculus mus. Aliquam imperdiet auctor mauris at congue. Donec quis odio
lobortis, posuere enim a, egestas odio. In hac habitasse platea dictumst.
Curabitur elementum quam neque. Vivamus ultrices lorem luctus risus congue
lacinia. Cras sodales tempus augue vel egestas. Curabitur a molestie velit.

### A subsection
Maecenas scelerisque dui id felis auctor varius. Integer aliquet pretium leo,
sed dapibus leo vestibulum ut. In sed scelerisque elit. Nullam nec ante ac felis
volutpat blandit. Nunc sagittis risus lectus. Nunc lorem massa, feugiat eget
convallis sed, tincidunt ut nisi. Duis nec mauris tincidunt, euismod neque
vitae, lobortis diam. Pellentesque quis elementum mauris, sed auctor ante. Fusce
faucibus venenatis pretium. $e^{i\theta} = \cos(\theta) + i\sin(\theta)$

$$
\begin{equation}
a + b = c
\end{equation}
$$

## Another section
Suspendisse ac massa sed orci vulputate iaculis nec
vel sapien. Pellentesque porta molestie risus, non tristique mi. Donec accumsan,
purus auctor tincidunt hendrerit, tortor magna finibus eros, luctus imperdiet mi
tellus nec tortor.

```python
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
```
