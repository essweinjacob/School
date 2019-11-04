float min(float *a, float N){
    float min = 1;

    for(int i = 0; i < N; i++){
        if(min > a[i]){
            min = a[i];
        }
    }

    return min;
}
