#include <cstring>
#include <chucknorris.h>

#include <ChuckNorris.hpp>

chuck_norris_t* chuck_norris_init()
{
    auto ck = new ChuckNorris();
    return reinterpret_cast<chuck_norris*>(ck);
}

char* chuck_norris_get_fact(chuck_norris_t* chuck_norris)
{
    auto ck = reinterpret_cast<ChuckNorris*>(chuck_norris);
    std::string fact = ck->getFact();
    char* result = _strdup(fact.c_str());
    return result;
}

void chuck_norris_deinit(chuck_norris_t * chuck_norris)
{
    auto ck = reinterpret_cast<ChuckNorris*>(chuck_norris);
    delete ck;
}