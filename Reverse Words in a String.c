void inline swap(char *s, int b, int e) {
    s[b] ^= s[e];
    s[e] ^= s[b];
    s[b] ^= s[e];
}

void reverse(char *s, int b, int e) {
    while (b < e) {
        swap(s, b++, e--);
    }
}

void trim(char *s, b, e) {
    while (s[b] == ' ') { b++; }
    while (s[e] == ' ') { e--; }
    int idx = 0;
    for (int i=b; i<=e; i++) {
        if (s[i] != ' ') {
            s[idx++] = s[i];
        } else if (s[i-1] != ' '){
            s[idx++] = ' ';
        }
    }
    s[idx] = '\0';
}

void reverseWords(char *s) {
    if (!s) {
        return;
    }
    int sz = strlen(s);
    reverse(s, 0, sz-1);
    int b=0, e=0;
    while (1) {
        if (!s[e] || s[e] == ' ') {
            reverse(s, b, e-1);
            while (s[e] && s[e] == ' ') { e++; }
            b = e;
            if (!s[e]) { break; }
        } else {
            e++;
        }
    }
    trim(s, b, sz-1);
}
