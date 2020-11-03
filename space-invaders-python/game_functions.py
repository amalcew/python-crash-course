import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, si_settings, stats, screen, play_button, ship, aliens, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(si_settings, screen, ship, bullets)
        else:
            start_game(si_settings, screen, stats, ship, aliens, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(si_settings, screen, stats, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, si_settings, stats, screen, play_button, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def start_game(si_settings, screen, stats, ship, aliens, bullets):
    """Start of the new game."""
    if not stats.game_active:
        si_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(si_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(si_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    if len(bullets) < si_settings.bullets_allowed:
        new_bullet = Bullet(si_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(si_settings, screen, ship, aliens, bullets):
    """Update position of bullets, get rid of old bullets."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(si_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(si_settings, screen, ship, aliens, bullets):
    """Reaction on collision between alien and a bullet."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        si_settings.increase_speed()
        create_fleet(si_settings, screen, ship, aliens)


def create_alien(si_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(si_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1.4 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.4*alien.rect.height*row_number
    aliens.add(alien)


def get_number_aliens_x(si_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = si_settings.screen_width - 1.4*alien_width
    number_alien_x = int(available_space_x/(1.4*alien_width))
    return number_alien_x


def get_number_rows(si_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (si_settings.screen_height - (4*alien_height) - ship_height)
    number_rows = int(available_space_y/(4*alien_height))
    return number_rows


def create_fleet(si_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(si_settings, screen)
    number_aliens_x = get_number_aliens_x(si_settings, alien.rect.width)
    number_rows = get_number_rows(si_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(si_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(si_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(si_settings, aliens)
            break


def change_fleet_direction(si_settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += si_settings.fleet_drop_speed
    si_settings.fleet_direction *= -1


def ship_hit(si_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(si_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(1)
    else:
        stats.game_active = False


def check_aliens_bottom(si_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(si_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(si_settings, stats, screen, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
      then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(si_settings, aliens)
    check_aliens_bottom(si_settings, stats, screen, ship, aliens, bullets)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(si_settings, stats, screen, ship, aliens, bullets)


def update_screen(screen, stats, bg, ship, aliens, bullets, play_button):
    """Update images on the screen, and flip to the new screen."""
    screen.blit(bg.image, bg.rect)

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()
