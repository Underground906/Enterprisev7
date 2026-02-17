import json

# Load both files
with open('C:/Users/under/Downloads/ENTERPRISE_OS_V7/07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/FULL_KIT_INVENTORY.json', encoding='utf-8') as f:
    inventory = json.load(f)

with open('C:/Users/under/Downloads/ENTERPRISE_OS_V7/07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/PRD_SCREEN_REQUIREMENTS.json', encoding='utf-8') as f:
    prd = json.load(f)

# Kit tier assignments
tier1 = {
    'Brainwave 2.0': 'dashboard shell',
    'Untitled UI Pro': 'design system',
    'Fleet Travel': 'top-level',
    'Source Fusion AI': 'AI chat',
    'Chroma': 'font stack/style',
    'Square Dashboard Desktop': 'data views',
    'Tripie Travel': 'platform front-end',
    'Briefberry': 'onboarding/presell'
}
tier2 = {
    'Huose Property': 'lead cards/property dash',
    'Zip Formate': 'pastels/graphs',
    'Social Dashboards': 'feeds/social',
    'Aitentico': 'collapsed sidebar',
    'Trakr': 'cool sidebar',
    'Caresync': 'green tones',
    'Aimate': 'promo',
    'Majin': 'promo',
    'Substance Dashboard': 'dashboard UI'
}
tier3 = {
    'Fitness Pro': 'fitness domain',
    'Finder (Directory & Listings)': 'directory',
    'Adify (Job Finding)': 'jobs',
    'eCommerce UI Kit': 'ecommerce'
}

# Platform-to-kit priority mapping
platform_kit_priority = {
    'property_platform': [
        'Brainwave 2.0', 'Untitled UI Pro', 'Huose Property', 'Real Estate SaaS Kit',
        'Square Dashboard Desktop', 'Chroma', 'Source Fusion AI', 'Triply AI',
        'Fleet Travel', 'Tripie Travel', 'Zip Formate', 'Social Dashboards',
        'Aitentico', 'Trakr', 'Briefberry', 'Nexus', 'Multi-concept Landing',
        'Stacks Design System', 'Substance Dashboard'
    ],
    'property_ai_apps': [
        'Source Fusion AI', 'Triply AI', 'Brainwave 2.0', 'Untitled UI Pro',
        'Huose Property', 'Real Estate SaaS Kit', 'Square Dashboard Desktop',
        'Zip Formate', 'Aitentico', 'Substance Dashboard'
    ],
    'fitness_platform': [
        'Fitness Pro', 'Brainwave 2.0', 'Untitled UI Pro', 'Triply AI',
        'Source Fusion AI', 'Square Dashboard Desktop', 'Zip Formate',
        'Befit', 'Caresync', 'Stacks Design System', 'Substance Dashboard'
    ]
}

all_kits = inventory['kits']

def score_kit_for_screen(kit_name, kit_data, screen, platform):
    score = 0
    reasons = []

    needed = set(screen.get('components_needed', []))
    kit_comps = set(kit_data.get('component_types', {}).keys())
    kit_layouts = set(kit_data.get('layout_types', {}).keys())

    # Component overlap
    overlap = needed & kit_comps
    comp_pct = (len(overlap) / len(needed) * 100) if needed else 0
    score += len(overlap) * 10

    # Layout match
    screen_layout = screen.get('layout', '').lower().replace('-', '_').replace(' ', '_')
    layout_map = {
        'sidebar_content': 'sidebar_content',
        'sidebar+content': 'sidebar_content',
        'split': 'split',
        'centered': 'centered',
        'grid': 'grid',
        'full_canvas': 'full_canvas',
        'full-canvas': 'full_canvas'
    }
    mapped_layout = layout_map.get(screen_layout, screen_layout)
    if mapped_layout in kit_layouts:
        score += 20
        reasons.append(f'layout:{mapped_layout}')

    # Tier bonus
    if kit_name in tier1:
        score += 15
    elif kit_name in tier2:
        score += 10
    elif kit_name in tier3:
        score += 5

    # Platform relevance bonus
    priority_kits = platform_kit_priority.get(platform, [])
    if kit_name in priority_kits:
        idx = priority_kits.index(kit_name)
        score += max(0, 20 - idx)

    # Screen richness bonus
    if kit_data['screen_count'] > 100:
        score += 5

    return {
        'score': score,
        'component_overlap': sorted(list(overlap)),
        'component_coverage_pct': round(comp_pct, 1),
        'missing_components': sorted(list(needed - kit_comps)),
        'reasons': reasons
    }

# Run matching
matching = {
    'generated_at': '2026-02-17',
    'methodology': 'Component type overlap + layout match + kit tier priority + platform relevance',
    'summary': {},
    'platforms': {}
}

total_matched = 0
total_full_coverage = 0

for platform_key, platform_data in prd['platforms'].items():
    platform_matches = []

    for screen in platform_data['screens']:
        screen_matches = []

        for kit_name, kit_data in all_kits.items():
            if kit_data['screen_count'] == 0:
                continue
            result = score_kit_for_screen(kit_name, kit_data, screen, platform_key)
            if result['score'] > 20:
                screen_matches.append({
                    'kit': kit_name,
                    **result
                })

        screen_matches.sort(key=lambda x: -x['score'])
        top5 = screen_matches[:5]

        has_full_coverage = any(m['component_coverage_pct'] >= 80 for m in top5)
        if has_full_coverage:
            total_full_coverage += 1
        total_matched += 1

        platform_matches.append({
            'screen_id': screen['screen_id'],
            'screen_name': screen['name'],
            'layout': screen.get('layout', ''),
            'components_needed': screen.get('components_needed', []),
            'priority': screen.get('priority', 'medium'),
            'top_kit_matches': top5,
            'best_coverage_pct': top5[0]['component_coverage_pct'] if top5 else 0,
            'has_80pct_coverage': has_full_coverage
        })

    matching['platforms'][platform_key] = {
        'total_screens': len(platform_matches),
        'screens_with_80pct_coverage': sum(1 for m in platform_matches if m['has_80pct_coverage']),
        'avg_best_coverage': round(sum(m['best_coverage_pct'] for m in platform_matches) / len(platform_matches), 1) if platform_matches else 0,
        'matches': platform_matches
    }

# Summary
matching['summary'] = {
    'total_prd_screens': total_matched,
    'screens_with_80pct_kit_coverage': total_full_coverage,
    'coverage_rate': f'{round(total_full_coverage/total_matched*100, 1)}%' if total_matched else '0%',
    'available_kits': len([k for k, v in all_kits.items() if v['screen_count'] > 0]),
    'available_screens': inventory['total_screens'],
    'available_components': inventory['total_component_instances']
}

for pk, pv in matching['platforms'].items():
    matching['summary'][f'{pk}_coverage'] = f'{pv["screens_with_80pct_coverage"]}/{pv["total_screens"]} screens at 80%+'

# Save
with open('C:/Users/under/Downloads/ENTERPRISE_OS_V7/07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/COMPONENT_TO_SCREEN_MATCHING.json', 'w', encoding='utf-8') as f:
    json.dump(matching, f, indent=2, ensure_ascii=False)

print('=== MATCHING COMPLETE ===')
print(f'Total PRD screens matched: {total_matched}')
print(f'Screens with 80%+ component coverage: {total_full_coverage} ({round(total_full_coverage/total_matched*100,1)}%)')
print()
for pk, pv in matching['platforms'].items():
    print(f'{pk}: {pv["screens_with_80pct_coverage"]}/{pv["total_screens"]} at 80%+ | avg best: {pv["avg_best_coverage"]}%')

# Also print top 5 most-needed kits across all platforms
kit_usage = {}
for pk, pv in matching['platforms'].items():
    for m in pv['matches']:
        for km in m['top_kit_matches'][:3]:
            kit_name = km['kit']
            kit_usage[kit_name] = kit_usage.get(kit_name, 0) + 1

print('\n=== MOST-REFERENCED KITS (top 3 match per screen) ===')
for name, count in sorted(kit_usage.items(), key=lambda x: -x[1])[:15]:
    tier = 'T1' if name in tier1 else ('T2' if name in tier2 else ('T3' if name in tier3 else 'Add'))
    print(f'  [{tier}] {name}: referenced {count} times')
