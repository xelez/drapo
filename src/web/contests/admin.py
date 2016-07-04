from django.contrib import admin

from . import models


class ContestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible_in_list', 'start_time', 'finish_time')
    list_display_links = ('id', )
    list_editable = ('is_visible_in_list', )
    search_fields = ('name', )


admin.site.register(models.TaskBasedContest, ContestAdmin)


class IndividualParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'contest', 'user')
    list_editable = ('id', 'contest')
    list_filter = ('contest', )

admin.site.register(models.IndividualParticipant, IndividualParticipantAdmin)


class TeamParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'contest', 'team')
    list_editable = ('id', 'contest')
    list_filter = ('contest',)

admin.site.register(models.TeamParticipant, TeamParticipantAdmin)


class ScoreByPlaceAdditionalScorerAdmin(admin.ModelAdmin):
    list_display = ('id', 'contest', 'place', 'points')
    list_editable = ('place', 'points')
    list_filter = ('contest', )

admin.site.register(models.ScoreByPlaceAdditionalScorer, ScoreByPlaceAdditionalScorerAdmin)


class ByCategoriesTasksOpeningPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'contest', 'opens_for_all_participants')
    list_editable = ('opens_for_all_participants', )
    list_filter = ('contest', )

admin.site.register(models.ByCategoriesTasksOpeningPolicy, ByCategoriesTasksOpeningPolicyAdmin)