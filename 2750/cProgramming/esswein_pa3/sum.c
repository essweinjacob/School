float sum (float *a, float N){
    float sum;
    for(int i = 0; i < N; i++){
        sum += a[i];
    }

    return sum;
}
