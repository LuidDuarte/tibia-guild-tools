from django.shortcuts import render, redirect, get_object_or_404

from guild_tracker.models import Guild

def list(request):
    guilds = Guild.objects.all()
    return render(request, 'list.html', context={'guilds': guilds})


def list_online_players(request):
    guild_name = request.GET.get('guild_name')
    guild = get_object_or_404(Guild, name=guild_name.replace('+', ' '))
    lists = guild.sort_by_priority()
    total_online = sum(map(lambda x: len(x.get('online')), lists))
    return render(request, 'online_players.html', 
                  context={'lists': guild.sort_by_priority(),
                           'online': total_online})