{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6ad167d0-996b-4dd9-acc4-2bad8ed2b45c",
   "metadata": {},
   "source": [
    "# Possible values of n and o for MWA"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "068de579-2dda-4e65-9448-72eafd34aa43",
   "metadata": {},
   "source": [
    "#### For people who are doing MWA may need to try different possible \"n\" (Number of SNe per bin) and \"o\" (overlap between bins) values. Also we need to find the bins that equally arrange the number of SNe.\n",
    "\n",
    "#### So here I have created a Python script you can use  to generate the all possible \"n\" and \"o\" values for your samples and u can generate the bins (numbers)\n",
    "\n",
    "#### Go through the .readme files for full explanation with theory."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d8c1ea8-5db0-4d0d-a8f5-3e1086536103",
   "metadata": {},
   "source": [
    "## Finding the n and o values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "330d5415-996c-4c96-b46c-e807ca522ebd",
   "metadata": {},
   "outputs": [],
   "source": [
    "T = 1829  # Number of SNe\n",
    "N = 20   # Number of bins\n",
    "\n",
    "# User inputs for the range of n\n",
    "min_n = 50\n",
    "max_n = 700\n",
    "\n",
    "# List to store valid (n, o) pairs\n",
    "valid_combinations = []\n",
    "\n",
    "# Iterate through the range of n values\n",
    "for n in range(min_n, max_n + 1):  \n",
    "    o = ((n * N) - T) / (N - 1)\n",
    "    \n",
    "    if o.is_integer() and o >= 0:  # Ensure o is a non-negative integer\n",
    "        valid_combinations.append((n, int(o)))\n",
    "\n",
    "# Print results\n",
    "if valid_combinations:\n",
    "    print(\"\\nPossible (n, o) values:\")\n",
    "    for n, o in valid_combinations:\n",
    "        print(f\"n = {n}, o = {o}\")\n",
    "else:\n",
    "    print(\"\\nNo valid (n, o) values found in the given range.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c66e046-51a9-4cbc-9985-603c79321338",
   "metadata": {},
   "source": [
    "## Bin seperation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34d821c6-56fa-4af9-85fe-a4ad0616f5eb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def define_bins(start, stop, o, bins, n):\n",
    "    bin_ranges = []\n",
    "    \n",
    "    for i in range(bins):\n",
    "        bin_start = start + i * (n - o)\n",
    "        bin_end = bin_start + n - 1\n",
    "        \n",
    "        if bin_end > stop:\n",
    "            bin_end = stop  # Ensure the last bin does not exceed the stop value\n",
    "        \n",
    "        bin_ranges.append((bin_start, bin_end))\n",
    "    \n",
    "    return bin_ranges\n",
    "\n",
    "# Example usage\n",
    "start = 1\n",
    "stop = 1829\n",
    "n = 537\n",
    "o = 469\n",
    "bins = 20\n",
    "\n",
    "\n",
    "ranges = define_bins(start, stop, o, bins, n)\n",
    "print(\"Bin Ranges:\")\n",
    "for i, (low, high) in enumerate(ranges, 1):\n",
    "    print(f\"Bin {i}: ({low}-{high})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "049ee2a3-3bf4-4558-82a0-9456a658f8ed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "6823c82a-1cf2-4ce2-bf8c-52b6c724d375",
   "metadata": {},
   "source": [
    " - - -"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bc6adc8-131d-4b7a-a7bb-fff1a62d0c58",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
