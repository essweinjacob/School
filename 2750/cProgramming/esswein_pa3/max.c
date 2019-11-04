float max(float *a, float N){
    float max = 0;
    for(int i = 0; i < N; i++){
        if(max < a[i]){
            max = a[i];
        }
    }

    return max;
}
