#include <stdio.h>
#include <stdlib.h>

int print_user_info(void)
{
    // my first c comment
    printf("Name   : Wesley Murray\n");
    printf("DOB    : August 12, 1881\n");
    printf("Mobile : 8329832932\n");
    return 0;
}

char* get_c_version(void)
{
    #if __STDC_VERSION__ >= 201710L
    return "C18";
    #elif __STDC_VERSION__ >= 201112L
    return "C11";
    #elif __STDC_VERSION__ >= 199901L
    return "C99";
    #else
    return "C89/C90";
    #endif
}

int main(int argc, char** argv)
{
    // variable assignment
    int num_calls = 2;
    int ret_codes_sum = 0;
    int *ret_codes = malloc(sizeof(int[num_calls]));

    // function calls
    ret_codes[0] = print_user_info();
    ret_codes[1] = printf("%s", get_c_version());

    // conditional
    for(int i=0; i<num_calls; i++)
    {
        ret_codes_sum += ret_codes[i];
    }
    if(ret_codes_sum)
    {
        return 1;
    }
    else 
    {
        return 0;
    }

    // free memory
    free(ret_codes);
}